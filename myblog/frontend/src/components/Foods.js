import React from 'react';
import { List, Card } from 'antd';

const Foods = (props) => {
    return (
      <List
        grid={{
          gutter: 16, xs: 1, sm: 2, md: 4, lg: 4, xl: 6, xxl: 3,
        }}
        dataSource={props.data}
        renderItem={item => (
          <List.Item>
            <Card title={<a href={`foods/${item.id}`}>{item.Name}</a>}>
                Source Type: {item.SourceType}
            </Card>
          </List.Item>
        )}
      />
    );
};

export default Foods;